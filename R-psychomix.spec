%global packname  psychomix
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Psychometric Mixture Models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-stats R-methods R-Formula R-flexmix R-psychotools 
Requires:         R-graphics R-stats R-lattice 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-methods R-Formula R-flexmix R-psychotools
BuildRequires:    R-graphics R-stats R-lattice 


%description
Psychometric mixture models based on flexmix infrastructure. At the moment
only Rasch mixture models are implemented in various flavors: with/without
concomitant variables, different parametrizations of the score
distribution (saturated vs. mean/variance specification). See
vignette("raschmix", package = "psychomix") for details.

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
%doc %{rlibdir}/psychomix/html
%doc %{rlibdir}/psychomix/NEWS
%doc %{rlibdir}/psychomix/DESCRIPTION
%doc %{rlibdir}/psychomix/doc
%{rlibdir}/psychomix/NAMESPACE
%{rlibdir}/psychomix/R
%{rlibdir}/psychomix/help
%{rlibdir}/psychomix/INDEX
%{rlibdir}/psychomix/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora