%global packname  gibbs.met
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          Naive Gibbs Sampling with Metropolis Steps

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provides two generic functions for performing Markov chain
sampling in a naive way for a user-defined target distribution, which
involves only continuous variables. The function "gibbs_met" performs
Gibbs sampling with each 1-dimensional distribution sampled with
Metropolis update using Gaussian proposal distribution centered at the
previous state. The function "met_gaussian" updates the whole state with
Metropolis method using independent Gaussian proposal distribution
centered at the previous state. The sampling is carried out without
considering any special tricks for improving efficiency. This package is
aimed at only routine applications of MCMC in moderate-dimensional

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
%doc %{rlibdir}/gibbs.met/html
%doc %{rlibdir}/gibbs.met/DESCRIPTION
%{rlibdir}/gibbs.met/INDEX
%{rlibdir}/gibbs.met/Meta
%{rlibdir}/gibbs.met/R
%{rlibdir}/gibbs.met/help
%{rlibdir}/gibbs.met/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.3-1
- initial package for Fedora