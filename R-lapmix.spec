%global packname  lapmix
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.20.0
Release:          1%{?dist}
Summary:          Laplace Mixture Model in Microarray Experiments

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 
Requires:         R-Biobase R-graphics R-grDevices R-methods R-stats R-tools R-utils 

BuildRequires:    R-devel tex(latex) R-stats
BuildRequires:    R-Biobase R-graphics R-grDevices R-methods R-stats R-tools R-utils 


%description
Laplace mixture modelling of microarray experiments. A hierarchical
Bayesian approach is used, and the hyperparameters are estimated using
empirical Bayes. The main purpose is to identify differentially expressed

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
%doc %{rlibdir}/lapmix/html
%doc %{rlibdir}/lapmix/DESCRIPTION
%doc %{rlibdir}/lapmix/doc
%{rlibdir}/lapmix/NAMESPACE
%{rlibdir}/lapmix/help
%{rlibdir}/lapmix/R
%{rlibdir}/lapmix/INDEX
%{rlibdir}/lapmix/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.20.0-1
- initial package for Fedora