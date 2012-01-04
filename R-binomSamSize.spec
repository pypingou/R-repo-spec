%global packname  binomSamSize
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Confidence intervals and sample size determination for a binomial proportion under simple random sampling and pooled sampling

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-binom 

BuildRequires:    R-devel tex(latex) R-binom 

%description
A suite of functions to compute confidence intervals and necessary sample
sizes for the parameter p of the Bernoulli B(p) distribution under simple
random sampling or under pooled sampling. Such computations are e.g. of
interest when investigating the incidence or prevalence in populations.
The package contains functions to compute coverage probabilities and
coverage coefficients of the provided confidence intervals procedures.
Sample size calculations are based on expected length.

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
%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora