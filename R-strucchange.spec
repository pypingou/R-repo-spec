%global packname  strucchange
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.6
Release:          1%{?dist}
Summary:          Testing, Monitoring, and Dating Structural Changes

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-stats R-zoo R-sandwich 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-zoo R-sandwich 

%description
Testing, monitoring and dating structural changes in (linear) regression
models. strucchange features tests/methods from the generalized
fluctuation test framework as well as from the F test (Chow test)
framework. This includes methods to fit, plot and test fluctuation
processes (e.g., CUSUM, MOSUM, recursive/moving estimates) and F
statistics, respectively. It is possible to monitor incoming data online
using fluctuation processes. Finally, the breakpoints in regression models
with structural changes can be estimated together with confidence
intervals. Emphasis is always given to methods for visualizing the data.

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
%doc %{rlibdir}/strucchange/CITATION
%doc %{rlibdir}/strucchange/DESCRIPTION
%doc %{rlibdir}/strucchange/NEWS
%doc %{rlibdir}/strucchange/doc
%doc %{rlibdir}/strucchange/html
%{rlibdir}/strucchange/help
%{rlibdir}/strucchange/INDEX
%{rlibdir}/strucchange/R
%{rlibdir}/strucchange/Meta
%{rlibdir}/strucchange/demo
%{rlibdir}/strucchange/NAMESPACE
%{rlibdir}/strucchange/data

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.6-1
- initial package for Fedora