%global packname  binMto
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.4
Release:          1%{?dist}
Summary:          Asymptotic simultaneous confidence intervals for many-to-one comparisons of proportions

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
Asymptotic simultaneous confidence intervals for comparison of many
treatments with one control, for the difference of binomial proportions,
allows for Dunnett-like-adjustment, Bonferroni or unadjusted intervals.
Simulation of power of the above interval methods, approximate calculation
of any-pair-power, and sample size iteration based on approximate any-pair
power. Exact conditional maximum test for many-to-one comparisons to a

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
%doc %{rlibdir}/binMto/html
%doc %{rlibdir}/binMto/DESCRIPTION
%{rlibdir}/binMto/INDEX
%{rlibdir}/binMto/Meta
%{rlibdir}/binMto/help
%{rlibdir}/binMto/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.4-1
- initial package for Fedora