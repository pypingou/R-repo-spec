%global packname  ergm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.4.3
Release:          1%{?dist}
Summary:          Fit, Simulate and Diagnose Exponential-Family Models for Networks

Group:            Applications/Engineering 
License:          GPL-3 + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.4-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-network R-nlme R-trust 

BuildRequires:    R-devel tex(latex) R-network R-nlme R-trust 

%description
An integrated set of tools to analyze and simulate networks based on
exponential-family random graph models (ERGM). "ergm" is a part of the
"statnet" suite of packages for network analysis.  For a list of functions
type: help(package='ergm')

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
%doc %{rlibdir}/ergm/CITATION
%doc %{rlibdir}/ergm/html
%doc %{rlibdir}/ergm/DESCRIPTION
%{rlibdir}/ergm/libs
%{rlibdir}/ergm/NEWS.Rd
%{rlibdir}/ergm/Meta
%{rlibdir}/ergm/data
%{rlibdir}/ergm/INDEX
%{rlibdir}/ergm/R
%{rlibdir}/ergm/help
%{rlibdir}/ergm/LICENSE
%{rlibdir}/ergm/NAMESPACE
%{rlibdir}/ergm/inst

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4.3-1
- initial package for Fedora