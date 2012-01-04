%global packname  DAMisc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Dave Armstrong's Miscellaneous Functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-effects R-sm R-rpanel 

BuildRequires:    R-devel tex(latex) R-effects R-sm R-rpanel 

%description
This package contains a few miscellaneous functions to help with the
presentation of linear model results.

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
%doc %{rlibdir}/DAMisc/DESCRIPTION
%doc %{rlibdir}/DAMisc/html
%{rlibdir}/DAMisc/data
%{rlibdir}/DAMisc/help
%{rlibdir}/DAMisc/INDEX
%{rlibdir}/DAMisc/R
%{rlibdir}/DAMisc/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora