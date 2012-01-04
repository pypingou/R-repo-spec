%global packname  dice
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Calculate probabilities of various dice-rolling events

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gtools 

BuildRequires:    R-devel tex(latex) R-gtools 

%description
This package provides utilities to calculate the probabilities of various
dice-rolling events, such as the probability of rolling a four-sided die
six times and getting a 4, a 3, and either a 1 or 2 among the six rolls
(in any order); the probability of rolling two six-sided dice three times
and getting a 10 on the first roll, followed by a 4 on the second roll,
followed by anything but a 7 on the third roll; or the probabilities of
each possible total of rolling five six-sided dice, dropping the lowest
two rolls, and summing the remaining dice.

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
%doc %{rlibdir}/dice/html
%doc %{rlibdir}/dice/DESCRIPTION
%{rlibdir}/dice/NAMESPACE
%{rlibdir}/dice/help
%{rlibdir}/dice/Meta
%{rlibdir}/dice/INDEX
%{rlibdir}/dice/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora