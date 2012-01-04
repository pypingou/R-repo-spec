%global packname  DiagnosisMed
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.3
Release:          1%{?dist}
Summary:          Diagnostic test accuracy evaluation for medical professionals.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-epitools R-TeachingDemos R-tcltk R-AMORE R-utils 

BuildRequires:    R-devel tex(latex) R-epitools R-TeachingDemos R-tcltk R-AMORE R-utils 

%description
DiagnosisMed is a package to analyze data from diagnostic test accuracy
evaluating health conditions. It is being built to be used by health
professionals. This package is able to estimate sensitivity and
specificity from categorical and continuous test results including some
evaluations of indeterminate results, or compare different categorical
tests, and estimate reasonble cut-offs of tests and display it in a way
commonly used by health professionals. No graphical interface is avalible
yet. Partners are most welcome.

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
%doc %{rlibdir}/DiagnosisMed/html
%doc %{rlibdir}/DiagnosisMed/DESCRIPTION
%{rlibdir}/DiagnosisMed/Meta
%{rlibdir}/DiagnosisMed/NAMESPACE
%{rlibdir}/DiagnosisMed/R
%{rlibdir}/DiagnosisMed/data
%{rlibdir}/DiagnosisMed/help
%{rlibdir}/DiagnosisMed/INDEX

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.3-1
- initial package for Fedora