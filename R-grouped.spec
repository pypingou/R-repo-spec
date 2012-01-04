%global packname  grouped
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.0
Release:          1%{?dist}
Summary:          Regression Analysis of Grouped and Coarse Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Regression models for grouped and coarse data, under the Coarsened At
Random assumption.

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
%doc %{rlibdir}/grouped/html
%doc %{rlibdir}/grouped/DESCRIPTION
%{rlibdir}/grouped/R
%{rlibdir}/grouped/NAMESPACE
%{rlibdir}/grouped/data
%{rlibdir}/grouped/INDEX
%{rlibdir}/grouped/Meta
%{rlibdir}/grouped/CHANGES
%{rlibdir}/grouped/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.0-1
- initial package for Fedora