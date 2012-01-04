%global packname  elrm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Exact Logistic Regression via MCMC

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-coda R-graphics R-stats 

BuildRequires:    R-devel tex(latex) R-coda R-graphics R-stats 

%description
elrm implements a Markov Chain Monte Carlo algorithm to approximate exact
conditional inference for logistic regression models. Exact conditional
inference is based on the distribution of the sufficient statistics for
the parameters of interest given the sufficient statistics for the
remaining nuisance parameters. Using model formula notation, users specify
a logistic model and model terms of interest for exact inference.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora