%global packname  locpol
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Kernel local polynomial regression

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Computes local polynomial estimators.

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
%doc %{rlibdir}/locpol/DESCRIPTION
%doc %{rlibdir}/locpol/html
%{rlibdir}/locpol/NAMESPACE
%{rlibdir}/locpol/help
%{rlibdir}/locpol/R
%{rlibdir}/locpol/INDEX
%{rlibdir}/locpol/Meta
%{rlibdir}/locpol/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.0-1
- initial package for Fedora