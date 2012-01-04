%global packname  AlgDesign
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.7
Release:          1%{?dist}
Summary:          Algorithmic Experimental Design

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Algorithmic experimental designs. Calculates exact and approximate theory
experimental designs for D,A, and I criteria. Very large designs may be
created. Experimental designs may be blocked or blocked designs created
from a candidate list, using several criteria.  The blocking can be done
when whole and within plot factors interact.

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
%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.7-1
- initial package for Fedora