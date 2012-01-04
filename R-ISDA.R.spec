%global packname  ISDA.R
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          interval symbolic data analysis for R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-scatterplot3d 

BuildRequires:    R-devel tex(latex) R-scatterplot3d 

%description
describes a set of operations for symbolic data type based on
interval-valued. The operations are processing of punctuals variables to
interval variables, construction of a 3D graphic interval, linear
regression interval and interval descriptive statistics such as mean,
median, variance, standard deviation and mode.

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
%doc %{rlibdir}/ISDA.R/DESCRIPTION
%doc %{rlibdir}/ISDA.R/html
%{rlibdir}/ISDA.R/NAMESPACE
%{rlibdir}/ISDA.R/R
%{rlibdir}/ISDA.R/INDEX
%{rlibdir}/ISDA.R/help
%{rlibdir}/ISDA.R/data
%{rlibdir}/ISDA.R/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora