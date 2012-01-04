%global packname  logcondiscr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Estimate a Log-Concave Probability Mass function from Discrete i.i.d. Observations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Matrix R-mvtnorm R-cobs 


BuildRequires:    R-devel tex(latex) R-Matrix R-mvtnorm R-cobs



%description
Given independent and identically distributed observations X(1), ...,
X(n), this package allows to compute the maximum likelihood estimator
(MLE) of probability mass function (pmf) under the assumption that it is
log-concave, see Weyermann (2007) and Balabdaoui, Jankowski, and Rufibach
(2011). The main functions of the package are 'logConDiscrMLE' that allows
computation of the log-concave MLE, 'logConDiscrCI' that computes
pointwise confidence bands for the MLE, and 'kInflatedLogConDiscr' that
computes a mixture of a log-concave PMF and a point mass at k.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora