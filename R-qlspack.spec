%global packname  qlspack
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Quasi Least Square Package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-geepack R-utils 

BuildRequires:    R-devel tex(latex) R-geepack R-utils 

%description
QLS is a two-stage computational approach for estimation of the
correlation parameters within the framework of GEE. It helps solving
parameters in mean, scale, and correlation structures for longitudinal

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
%doc %{rlibdir}/qlspack/DESCRIPTION
%doc %{rlibdir}/qlspack/html
%{rlibdir}/qlspack/R
%{rlibdir}/qlspack/NAMESPACE
%{rlibdir}/qlspack/INDEX
%{rlibdir}/qlspack/help
%{rlibdir}/qlspack/data
%{rlibdir}/qlspack/Meta

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2-1
- initial package for Fedora