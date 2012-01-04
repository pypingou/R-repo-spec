%global packname  anesrake
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.70
Release:          1%{?dist}
Summary:          ANES Raking Implementation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Hmisc 

BuildRequires:    R-devel tex(latex) R-Hmisc 

%description
This package provides a comprehensive system for selecting variables and
weighting data to match the specifications of the American National
Election Studies.  The package includes methods for identifying discrepant
variables, raking data, and assessing the effects of the raking algorithm.
 It also allows automated re-raking if target variables fall outside
identified bounds and allows greater user specification than other
available raking algorithms. A variety of simple weighted statistics that
were previously in this package (version .55 and earlier) have been moved
to the package 'weights.'

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
%doc %{rlibdir}/anesrake/DESCRIPTION
%doc %{rlibdir}/anesrake/html
%{rlibdir}/anesrake/R
%{rlibdir}/anesrake/INDEX
%{rlibdir}/anesrake/help
%{rlibdir}/anesrake/data
%{rlibdir}/anesrake/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.70-1
- initial package for Fedora