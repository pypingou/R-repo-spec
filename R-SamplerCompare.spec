%global packname  SamplerCompare
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.2
Release:          1%{dist}
Summary:          A framework for comparing the performance of MCMC samplers

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
This package consists of two components: a framework for running sets of
MCMC samplers on sets of distributions with a variety of tuning parameters
and plotting functions to visualize the results of those simulations.  See
sc-intro.pdf for an introduction.  Version 1.2 adds a mechanism for
loading external simulations.

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
%doc %{rlibdir}/SamplerCompare/doc
%doc %{rlibdir}/SamplerCompare/CITATION
%doc %{rlibdir}/SamplerCompare/DESCRIPTION
%doc %{rlibdir}/SamplerCompare/html
%{rlibdir}/SamplerCompare/INDEX
%{rlibdir}/SamplerCompare/include
%{rlibdir}/SamplerCompare/help
%{rlibdir}/SamplerCompare/libs
%{rlibdir}/SamplerCompare/NAMESPACE
%{rlibdir}/SamplerCompare/Meta
%{rlibdir}/SamplerCompare/R

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.2-1
- Update to version 1.2.2

* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora