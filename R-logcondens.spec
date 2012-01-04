%global packname  logcondens
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.4
Release:          1%{?dist}
Summary:          Estimate a Log-Concave Probability Density from iid Observations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Given independent and identically distributed observations X(1), ...,
X(n), this package allows to compute the maximum likelihood estimator
(MLE) of a density as well as a smoothed version of it under the
assumption that the density is log-concave, see Rufibach (2007) and
Duembgen and Rufibach (2009). The main function of the package is
'logConDens' that allows computation of the log-concave MLE and its
smoothed version. In addition, we provide functions to compute (1) the
value of the density and distribution function estimates (MLE and
smoothed) at a given point (2) the characterizing functions of the
estimator, (3) to sample from the estimated distribution, (5) to compute a
two-sample permutation test based on log-concave densities, (6) the ROC
curve based on log-concave estimates within cases and controls. Finally,
three datasets that have been used to illustrate log-concave density
estimation are made available.

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
%doc %{rlibdir}/logcondens/DESCRIPTION
%doc %{rlibdir}/logcondens/CITATION
%doc %{rlibdir}/logcondens/NEWS
%doc %{rlibdir}/logcondens/doc
%doc %{rlibdir}/logcondens/html
%{rlibdir}/logcondens/data
%{rlibdir}/logcondens/NAMESPACE
%{rlibdir}/logcondens/R
%{rlibdir}/logcondens/Meta
%{rlibdir}/logcondens/INDEX
%{rlibdir}/logcondens/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.4-1
- initial package for Fedora