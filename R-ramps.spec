%global packname  ramps
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.10
Release:          1%{?dist}
Summary:          Bayesian Geostatistical Modeling with RAMPS

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-coda R-fields R-Matrix R-maps R-methods R-nlme 

BuildRequires:    R-devel tex(latex) R-coda R-fields R-Matrix R-maps R-methods R-nlme 

%description
Bayesian geostatistical modeling of Gaussian processes using a
reparameterized and marginalized posterior sampling (RAMPS) algorithm
designed to lower autocorrelation in MCMC samples.  Package performance is
tuned for large spatial datasets.

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
%doc %{rlibdir}/ramps/CITATION
%doc %{rlibdir}/ramps/DESCRIPTION
%doc %{rlibdir}/ramps/html
%{rlibdir}/ramps/NAMESPACE
%{rlibdir}/ramps/help
%{rlibdir}/ramps/data
%{rlibdir}/ramps/INDEX
%{rlibdir}/ramps/Meta
%{rlibdir}/ramps/R

%changelog
* Wed Nov 23 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.10-1
- initial package for Fedora