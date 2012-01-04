%global packname  QCA3
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.4
Release:          1%{?dist}
Summary:          Yet another package for Qualitative Comparative Analysis

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-lpSolve 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-lpSolve 


%description
A set of functions for Qulitative Comparative Analysis (QCA). It can be
used for various types of QCA (csQCA, mvQCA fsQCA and crip set TQCA and
time-serious QCA). It has methods for simplifying assumption,
contradictory simplifying assumption.

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
%doc %{rlibdir}/QCA3/CITATION
%doc %{rlibdir}/QCA3/DESCRIPTION
%doc %{rlibdir}/QCA3/html
%{rlibdir}/QCA3/NAMESPACE
%{rlibdir}/QCA3/RoscignoHodson.Rdata
%{rlibdir}/QCA3/TODO
%{rlibdir}/QCA3/Meta
%{rlibdir}/QCA3/Fink.Hafnera.Rdata
%{rlibdir}/QCA3/R
%{rlibdir}/QCA3/ChangLog
%{rlibdir}/QCA3/help
%{rlibdir}/QCA3/License
%{rlibdir}/QCA3/Profiling.R
RPM build errors:
%{rlibdir}/QCA3/INDEX
%{rlibdir}/QCA3/data

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.4-1
- initial package for Fedora