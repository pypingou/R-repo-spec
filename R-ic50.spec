%global packname  ic50
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.2
Release:          1%{?dist}
Summary:          Standardized high-throughput evaluation of cell-based compound screens

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk 

BuildRequires:    R-devel tex(latex) R-tcltk 

%description
Calculation of IC50 values, automatic drawing of dose-response curves and
validation of compound screens on 96- and 384-well plates.

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
%doc %{rlibdir}/ic50/html
%doc %{rlibdir}/ic50/doc
%doc %{rlibdir}/ic50/DESCRIPTION
%{rlibdir}/ic50/INDEX
%{rlibdir}/ic50/design
%{rlibdir}/ic50/NAMESPACE
%{rlibdir}/ic50/Meta
%{rlibdir}/ic50/R
%{rlibdir}/ic50/data
%{rlibdir}/ic50/nsclc
%{rlibdir}/ic50/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.2-1
- initial package for Fedora