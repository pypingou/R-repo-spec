%global packname  norm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.9.2
Release:          1%{?dist}
Summary:          Analysis of multivariate normal datasets with missing values

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-9.2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Analysis of multivariate normal datasets with missing values

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
%doc %{rlibdir}/norm/html
%doc %{rlibdir}/norm/DESCRIPTION
%{rlibdir}/norm/R
%{rlibdir}/norm/LICENSE
%{rlibdir}/norm/help
%{rlibdir}/norm/INDEX
%{rlibdir}/norm/libs
%{rlibdir}/norm/data
%{rlibdir}/norm/NAMESPACE
%{rlibdir}/norm/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.9.2-1
- initial package for Fedora