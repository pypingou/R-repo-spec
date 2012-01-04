%global packname  TEQR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Target Equavelence Range Design

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The target equivalence range (TEQR) design is a frequentist implementation
of the modified toxicity probability interval (mTPI) design and a
competitor to the standard 3+3 design (3+3).  The 3+3 is the work horse
design in Phase I. It is good at determining if a safe dose exits, but
provides poor accuracy and precision in estimating the level of toxicity
at the maximum tolerated dose (MTD).  The TEQR is better than the 3+3 when
compared on: 1) the number of times the dose at or nearest the target
toxicity level was selected as the MTD, 2) the number of subjects assigned
to doses levels, at or nearest the MTD, and 3) the overall trial DLT rate.
TEQR more accurately and more precisely estimates the rate of toxicity at
the MTD because a larger number of subjects are studied at the MTD dose.
The TEQR on average uses fewer subjects and provide reasonably comparable
results to the continual reassessment method (CRM) in the number of times
the dose at or nearest the target toxicity level was selected as the MTD
and the number of subjects assigned doses, at, or nearest the target and
in overall DLT rate.

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
%doc %{rlibdir}/TEQR/DESCRIPTION
%doc %{rlibdir}/TEQR/html
%{rlibdir}/TEQR/Meta
%{rlibdir}/TEQR/INDEX
%{rlibdir}/TEQR/R
%{rlibdir}/TEQR/NAMESPACE
%{rlibdir}/TEQR/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora