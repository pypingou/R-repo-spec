%global packname  influence.ME
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8.1
Release:          1%{?dist}
Summary:          Tools for detecting influential data in mixed effects models

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lme4 R-lattice 


BuildRequires:    R-devel tex(latex) R-lme4 R-lattice



%description
influence.ME provides a collection of tools for calculating measures of
influential data for mixed effects models. It analyses models that were
estimated using lme4. The basic rationale behind identifying influential
data is that when iteratively single units are omitted from the data,
models based on these data should not produce substantially different
estimates. To standardize the assessment of how influential a (single
group of) observation(s) is, several measures of influence are common
practice. First, DFBETAS is a standardized measure of the absolute
difference between the estimate with a particular case included and the
estimate without that particular case. Second, Cook's distance provides an
overall measurement of the change in all parameter estimates, or a
selection thereof.

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
%doc %{rlibdir}/influence.ME/html
%doc %{rlibdir}/influence.ME/DESCRIPTION
%{rlibdir}/influence.ME/INDEX
%{rlibdir}/influence.ME/R
%{rlibdir}/influence.ME/help
%{rlibdir}/influence.ME/Meta
%{rlibdir}/influence.ME/NAMESPACE
%{rlibdir}/influence.ME/data

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.1-1
- initial package for Fedora