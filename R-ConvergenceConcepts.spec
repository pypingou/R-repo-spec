%global packname  ConvergenceConcepts
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Seeing convergence concepts in action

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tkrplot R-lattice 

BuildRequires:    R-devel tex(latex) R-tkrplot R-lattice 

%description
This package provides a way to investigate various modes of convergence of
random variables.

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
%doc %{rlibdir}/ConvergenceConcepts/CITATION
%doc %{rlibdir}/ConvergenceConcepts/DESCRIPTION
%doc %{rlibdir}/ConvergenceConcepts/html
%{rlibdir}/ConvergenceConcepts/help
%{rlibdir}/ConvergenceConcepts/R
%{rlibdir}/ConvergenceConcepts/HISTORY
%{rlibdir}/ConvergenceConcepts/INDEX
%{rlibdir}/ConvergenceConcepts/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora