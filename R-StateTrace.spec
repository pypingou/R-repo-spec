%global packname  StateTrace
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Bayesian Ordinal Analysis for State Trace Designs

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-KernSmooth R-coda R-fgui 


BuildRequires:    R-devel tex(latex) R-KernSmooth R-coda R-fgui



%description
StateTrace automates many aspects of a state-trace analysis of accuracy
and other binary response data, including implementing Bayesian methods
quantifying evidence about the outcomes of a state-trace experiment and
the creation of customisable graphs. It also offers users either a GUI or
non-GUI (i.e., command line input) implementation of the contained

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
%doc %{rlibdir}/StateTrace/html
%doc %{rlibdir}/StateTrace/DESCRIPTION
%doc %{rlibdir}/StateTrace/doc
%doc %{rlibdir}/StateTrace/CITATION
%{rlibdir}/StateTrace/Meta
%{rlibdir}/StateTrace/NAMESPACE
%{rlibdir}/StateTrace/data
%{rlibdir}/StateTrace/R
RPM build errors:
%{rlibdir}/StateTrace/INDEX
%{rlibdir}/StateTrace/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora