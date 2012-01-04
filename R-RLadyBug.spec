%global packname  RLadyBug
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.1
Release:          1%{?dist}
Summary:          Analysis of Infectious Diseases using Stochastic Epidemic Models

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-rJava R-coda 
Requires:         R-graphics R-stats R-grDevices R-utils R-MASS R-boa R-quadprog 

BuildRequires:    R-devel tex(latex) R-methods R-rJava R-coda
BuildRequires:    R-graphics R-stats R-grDevices R-utils R-MASS R-boa R-quadprog 


%description
The package consists of two independent tools to analyse infectious
disease surveillance data: 1. Stochastic
Susceptible-Exposed-Infectious-Recovered (SEIR) models are treated by the
java program LadyBug, i.e. for use of this functionality of the package a
java virtual machine has to be installed on your computer. 2. Multivariate
temporal counting processes for a fixed set of locations are modeled
through additive-multiplicative conditional intensities (fitted by the
'twinSIR' function).

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
%doc %{rlibdir}/RLadyBug/CITATION
%doc %{rlibdir}/RLadyBug/NEWS
%doc %{rlibdir}/RLadyBug/DESCRIPTION
%doc %{rlibdir}/RLadyBug/html
%{rlibdir}/RLadyBug/data
%{rlibdir}/RLadyBug/INDEX
%{rlibdir}/RLadyBug/R
%{rlibdir}/RLadyBug/help
%{rlibdir}/RLadyBug/demo
%{rlibdir}/RLadyBug/NAMESPACE
%{rlibdir}/RLadyBug/LICENSE
%{rlibdir}/RLadyBug/LadyBug
%{rlibdir}/RLadyBug/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.1-1
- initial package for Fedora