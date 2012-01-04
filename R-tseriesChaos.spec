%global packname  tseriesChaos
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.11
Release:          1%{?dist}
Summary:          Analysis of nonlinear time series

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-odesolve 

BuildRequires:    R-devel tex(latex) R-odesolve 

%description
Routines for the analysis of nonlinear time series. This work is largely
inspired by the TISEAN project, by Rainer Hegger, Holger Kantz and Thomas
Schreiber: http://www.mpipks-dresden.mpg.de/~tisean/

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
%doc %{rlibdir}/tseriesChaos/html
%doc %{rlibdir}/tseriesChaos/DESCRIPTION
%{rlibdir}/tseriesChaos/Meta
%{rlibdir}/tseriesChaos/data
%{rlibdir}/tseriesChaos/NAMESPACE
%{rlibdir}/tseriesChaos/libs
%{rlibdir}/tseriesChaos/help
%{rlibdir}/tseriesChaos/ChangeLog
%{rlibdir}/tseriesChaos/INDEX
%{rlibdir}/tseriesChaos/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.11-1
- initial package for Fedora