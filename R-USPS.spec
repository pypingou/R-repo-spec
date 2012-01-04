%global packname  USPS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Unsupervised and Supervised methods of Propensity Score Adjustment for Bias

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-cluster R-lattice R-gss 


BuildRequires:    R-devel tex(latex) R-cluster R-lattice R-gss



%description
Unsupervised methods: identify and display the distribution of Local
Treatment Differences (LTDs) and Local Average Treatment Effects (LATEs)
across Clusters of patients chosen so as to be relatively well matched on
patient baseline X-covariates.  Supervised methods: estimate and validate
Propensity Scores and use them to either sub-group or smooth observed
patient outcomes over the common support of alternative treatment cohorts.

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
%doc %{rlibdir}/USPS/DESCRIPTION
%doc %{rlibdir}/USPS/html
%{rlibdir}/USPS/R
%{rlibdir}/USPS/help
%{rlibdir}/USPS/INDEX
%{rlibdir}/USPS/NAMESPACE
%{rlibdir}/USPS/USPSinR.pdf
%{rlibdir}/USPS/data
%{rlibdir}/USPS/demo
%{rlibdir}/USPS/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora