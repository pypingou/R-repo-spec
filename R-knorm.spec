%global packname  knorm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Microarray Data From Multiple Biologically Interrelated Experiments

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
This package provides Knorm correlations between genes (or probes) from
microarray data obtained across multiple biologically interrelated
experiments.  The Knorm correlation adjusts for experiment dependencies
(correlations) and reduces to the Pearson coefficient when experiment
dependencies are absent.  The Knorm estimation approach can be generally
applicable to obtain between-row correlations from data matrices with
two-way dependencies.

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
%doc %{rlibdir}/knorm/DESCRIPTION
%doc %{rlibdir}/knorm/html
%{rlibdir}/knorm/data
%{rlibdir}/knorm/Meta
%{rlibdir}/knorm/NAMESPACE
%{rlibdir}/knorm/R
%{rlibdir}/knorm/INDEX
%{rlibdir}/knorm/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora