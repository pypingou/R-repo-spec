%global packname  CCA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Canonical correlation analysis

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-fda R-fields 

BuildRequires:    R-devel tex(latex) R-fda R-fields 

%description
The package provide a set of functions that extend the cancor function
with new numerical and graphical outputs. It also include a regularized
extension of the cannonical correlation analysis to deal with datasets
with more variables than observations.

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
%doc %{rlibdir}/CCA/DESCRIPTION
%doc %{rlibdir}/CCA/html
%{rlibdir}/CCA/help
%{rlibdir}/CCA/data
%{rlibdir}/CCA/Meta
%{rlibdir}/CCA/R
%{rlibdir}/CCA/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora