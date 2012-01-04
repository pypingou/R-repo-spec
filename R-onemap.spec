%global packname  onemap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Software for constructing genetic maps in experimental crosses: full-sib, RILs, F2 and backcrosses

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk R-tkrplot 

BuildRequires:    R-devel tex(latex) R-tcltk R-tkrplot 

%description
Analysis of molecular marker data from model (backcrosses, F2 and
recombinant inbred lines) and non-model systems (i. e. outcrossing
species). For the later, it allows statistical analysis by simultaneously
estimating linkage and linkage phases (genetic map construction). All
analysis are based on multipoint approaches using hidden Markov models.

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
%doc %{rlibdir}/onemap/CITATION
%doc %{rlibdir}/onemap/DESCRIPTION
%doc %{rlibdir}/onemap/doc
%doc %{rlibdir}/onemap/html
%{rlibdir}/onemap/INDEX
%{rlibdir}/onemap/HISTORY.txt
%{rlibdir}/onemap/help
%{rlibdir}/onemap/Meta
%{rlibdir}/onemap/libs
%{rlibdir}/onemap/example
%{rlibdir}/onemap/BUGS.txt
%{rlibdir}/onemap/data
%{rlibdir}/onemap/NAMESPACE
%{rlibdir}/onemap/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.1-1
- initial package for Fedora