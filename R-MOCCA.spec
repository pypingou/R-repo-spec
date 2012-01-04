%global packname  MOCCA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Multi-objective optimization for collecting cluster alternatives

Group:            Applications/Engineering 
License:          Artistic License 2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-cclust R-clv 

BuildRequires:    R-devel tex(latex) R-cclust R-clv 

%description
This package provides methods to analyze cluster alternatives based on
multi-objective optimization of cluster validation indices.

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
%doc %{rlibdir}/MOCCA/html
%doc %{rlibdir}/MOCCA/DESCRIPTION
%{rlibdir}/MOCCA/help
%{rlibdir}/MOCCA/INDEX
%{rlibdir}/MOCCA/Meta
%{rlibdir}/MOCCA/NAMESPACE
%{rlibdir}/MOCCA/R
%{rlibdir}/MOCCA/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora