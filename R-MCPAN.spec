%global packname  MCPAN
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.13
Release:          1%{?dist}
Summary:          Multiple comparisons using normal approximation

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-13.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm R-multcomp 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-multcomp 

%description
Multiple contrast tests and simultaneous confidence intervals based on
normal approximation. With implementations for binomial proportions in a
2xk setting (risk difference and odds ratio), poly-3-adjusted tumour
rates, biodiversity indices and expected values under lognormal
assumption. Approximative power calculation for multiple contrast tests of
binomial proportions.

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
%doc %{rlibdir}/MCPAN/html
%doc %{rlibdir}/MCPAN/DESCRIPTION
%{rlibdir}/MCPAN/help
%{rlibdir}/MCPAN/data
%{rlibdir}/MCPAN/R
%{rlibdir}/MCPAN/INDEX
%{rlibdir}/MCPAN/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.13-1
- initial package for Fedora