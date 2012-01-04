%global packname  HiddenMarkov
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          Hidden Markov Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Contains functions for the analysis of Discrete Time Hidden Markov Models,
Markov Modulated GLMs and the Markov Modulated Poisson Process. It
includes functions for simulation, parameter estimation, and the Viterbi
algorithm. See the topic "HiddenMarkov" for an introduction to the
package, and "Changes" for a list of recent changes. The algorithms are
based of those of Walter Zucchini.

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
%doc %{rlibdir}/HiddenMarkov/html
%doc %{rlibdir}/HiddenMarkov/CITATION
%doc %{rlibdir}/HiddenMarkov/DESCRIPTION
%doc %{rlibdir}/HiddenMarkov/doc
%{rlibdir}/HiddenMarkov/INDEX
%{rlibdir}/HiddenMarkov/demo
%{rlibdir}/HiddenMarkov/NAMESPACE
%{rlibdir}/HiddenMarkov/help
%{rlibdir}/HiddenMarkov/libs
%{rlibdir}/HiddenMarkov/R
%{rlibdir}/HiddenMarkov/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.0-1
- initial package for Fedora