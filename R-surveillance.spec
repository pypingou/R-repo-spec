%global packname  surveillance
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Modeling and monitoring discrete response time series

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-utils R-xtable R-spc R-sp R-maptools R-vcd R-msm R-Matrix 

BuildRequires:    R-devel tex(latex) R-methods R-utils R-xtable R-spc R-sp R-maptools R-vcd R-msm R-Matrix 

%description
A package implementing statistical methods for the modeling and
change-point detection in time series of counts, proportions and
categorical data. Focus is on outbreak detection in count data time series
originating from public health surveillance of infectious diseases, but
applications could just as well originate from environmetrics, reliability
engineering, econometrics or social sciences.  Currently the package
contains implementations typical outbreak detection procedures such as
Stroup et. al (1989), Farrington et al, (1996), Rossi et al. (1999),
Rogerson and Yamada (2001), a Bayesian approach, negative binomial CUSUM
methods and a detector based on generalized likelihood ratios.
Furthermore, inference methods for the retrospective infectious disease
model in Held et al. (2005), Held et al. (2006) and Paul et al. (2008) are
provided. A novel CUSUM approach combining logistic and multinomial
logistic modelling is also included. The package contains several
real-world datasets, the ability to simulate outbreak data, visualize the
results of the monitoring in temporal, spatial or spatio-temporal fashion.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora