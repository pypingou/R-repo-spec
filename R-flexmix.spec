%global packname  flexmix
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.3.5
Release:          1%{?dist}
Summary:          Flexible Mixture Modeling

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.3-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-modeltools R-multcomp 
Requires:         R-methods R-stats R-stats4 

BuildRequires:    R-devel tex(latex) R-lattice R-modeltools R-multcomp
BuildRequires:    R-methods R-stats R-stats4 


%description
FlexMix implements a general framework for finite mixtures of regression
models using the EM algorithm. FlexMix provides the E-step and all data
handling, while the M-step can be supplied by the user to easily define
new models. Existing drivers implement mixtures of standard linear models,
generalized linear models and model-based clustering.

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
%doc %{rlibdir}/flexmix/CITATION
%doc %{rlibdir}/flexmix/NEWS
%doc %{rlibdir}/flexmix/doc
%doc %{rlibdir}/flexmix/html
%doc %{rlibdir}/flexmix/DESCRIPTION
%{rlibdir}/flexmix/help
%{rlibdir}/flexmix/NAMESPACE
%{rlibdir}/flexmix/INDEX
%{rlibdir}/flexmix/Meta
%{rlibdir}/flexmix/R
%{rlibdir}/flexmix/data

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.5-1
- initial package for Fedora