%global packname  foreign
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.47
Release:          1%{?dist}
Summary:          Read Data Stored by Minitab, S, SAS, SPSS, Stata, Systat, dBase, ...

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-47.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Functions for reading and writing data stored by statistical packages such
as Minitab, S, SAS, SPSS, Stata, Systat, ..., and for reading and writing
dBase files.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/foreign/DESCRIPTION
%doc %{rlibdir}/foreign/LICENCE
%doc %{rlibdir}/foreign/html
%{rlibdir}/foreign/INDEX
%{rlibdir}/foreign/R
%{rlibdir}/foreign/po
%{rlibdir}/foreign/files
%{rlibdir}/foreign/NAMESPACE
%{rlibdir}/foreign/libs
%{rlibdir}/foreign/help
%{rlibdir}/foreign/Meta

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.47-1
- initial package for Fedora