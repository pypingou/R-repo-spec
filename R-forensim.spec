%global packname  forensim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Statistical tools for the interpretation of forensic DNA mixtures

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Statistical methods and simulation tools for the interpretation of
forensic DNA mixtures

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
%doc %{rlibdir}/forensim/doc
%doc %{rlibdir}/forensim/html
%doc %{rlibdir}/forensim/DESCRIPTION
%{rlibdir}/forensim/NAMESPACE
%{rlibdir}/forensim/files
%{rlibdir}/forensim/Meta
%{rlibdir}/forensim/help
%{rlibdir}/forensim/INDEX
RPM build errors:
%{rlibdir}/forensim/data
%{rlibdir}/forensim/libs
%{rlibdir}/forensim/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora