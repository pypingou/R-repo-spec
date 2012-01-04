%global packname  paleoTS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Analyze paleontological time-series

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
This package facilitates analysis of paleontological sequences of trait
values from an evolving lineage.  Functions are provided to fit, using
maximum likelihood, evolutionary models including unbiased random walks,
directional evolution, stasis, Ornstein-Uhlenbeck, punctuated change, and
evolutionary models in which traits track some measured covariate.

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
%doc %{rlibdir}/paleoTS/DESCRIPTION
%doc %{rlibdir}/paleoTS/html
%{rlibdir}/paleoTS/data
%{rlibdir}/paleoTS/help
%{rlibdir}/paleoTS/R
%{rlibdir}/paleoTS/INDEX
%{rlibdir}/paleoTS/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.1-1
- initial package for Fedora