%global packname  pan
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Multiple imputation for multivariate panel or clustered data

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Multiple imputation for multivariate panel or clustered data

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
%doc %{rlibdir}/pan/DESCRIPTION
%doc %{rlibdir}/pan/html
%doc %{rlibdir}/pan/doc
%{rlibdir}/pan/libs
%{rlibdir}/pan/INDEX
%{rlibdir}/pan/help
%{rlibdir}/pan/Meta
%{rlibdir}/pan/LICENSE
%{rlibdir}/pan/NAMESPACE
%{rlibdir}/pan/tests
%{rlibdir}/pan/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora