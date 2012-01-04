%global packname  PowerTOST
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.7
Release:          1%{?dist}
Summary:          Power and Sample size based on two one-sided t-tests (TOST) for bioequivalence studies

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-stats R-mvtnorm 

%description
Contains functions to calculate power and sample size for various study
designs used for bioequivalence studies.  See function known.designs() for
study designs covered.  Moreover the package contains functions for power
and sample size based on 'expected' power in case of uncertain (estimated)
variability.  Added are functions for the power and sample size for the
ratio of two means with normally distributed data on the original scale
(based on Fieller's confidence ('fiducial') interval).

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
%doc %{rlibdir}/PowerTOST/doc
%doc %{rlibdir}/PowerTOST/DESCRIPTION
%doc %{rlibdir}/PowerTOST/html
%doc %{rlibdir}/PowerTOST/NEWS
%{rlibdir}/PowerTOST/help
%{rlibdir}/PowerTOST/NAMESPACE
%{rlibdir}/PowerTOST/R
%{rlibdir}/PowerTOST/INDEX
%{rlibdir}/PowerTOST/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.7-1
- initial package for Fedora