%global packname  lorec
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6
Release:          1%{?dist}
Summary:          LOw Rand and sparsE Covariance matrix estimation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Estimate covariance matrices that contain low rank and sparse components

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/lorec/DESCRIPTION
%doc %{rlibdir}/lorec/html
%{rlibdir}/lorec/help
%{rlibdir}/lorec/INDEX
%{rlibdir}/lorec/Meta
%{rlibdir}/lorec/NAMESPACE
%{rlibdir}/lorec/libs
%{rlibdir}/lorec/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6-1
- initial package for Fedora