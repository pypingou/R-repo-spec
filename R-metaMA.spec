%global packname  metaMA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Meta-analysis for MicroArrays

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-limma R-SMVar 

BuildRequires:    R-devel tex(latex) R-limma R-SMVar 

%description
Combines either p-values or modified effect sizes from different studies
to find differentially expressed genes

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
%doc %{rlibdir}/metaMA/DESCRIPTION
%doc %{rlibdir}/metaMA/html
%{rlibdir}/metaMA/data
%{rlibdir}/metaMA/help
%{rlibdir}/metaMA/R
%{rlibdir}/metaMA/INDEX
%{rlibdir}/metaMA/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1-1
- initial package for Fedora