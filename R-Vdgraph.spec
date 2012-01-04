%global packname  Vdgraph
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          This package creates variance dispersion graphs for response surface designs

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rsm 

BuildRequires:    R-devel tex(latex) R-rsm 

%description
This package calls a modification of the published FORTRAN code for
producing variance dispersion graphs. For more details on variance
dispersion graphs see "A Computer Program for Generating Variance
Dispersion Graphs" by G. Vining, Journal of Quality Technology, Vol. 25
No. 1 January 1993.

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
%doc %{rlibdir}/Vdgraph/html
%doc %{rlibdir}/Vdgraph/DESCRIPTION
%{rlibdir}/Vdgraph/Meta
%{rlibdir}/Vdgraph/libs
%{rlibdir}/Vdgraph/R
%{rlibdir}/Vdgraph/NAMESPACE
%{rlibdir}/Vdgraph/help
%{rlibdir}/Vdgraph/data
%{rlibdir}/Vdgraph/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora