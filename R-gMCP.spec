%global packname  gMCP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.1
Release:          1%{?dist}
Summary:          Graph Based Multiple Comparison Procedures

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rJava R-CommonJavaJars R-methods R-MASS R-PolynomF R-multcomp R-JavaGD R-lattice 

BuildRequires:    R-devel tex(latex) R-rJava R-CommonJavaJars R-methods R-MASS R-PolynomF R-multcomp R-JavaGD R-lattice 

%description
This package provides functions and a graphical user interface for
graphical described multiple test procedures.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.1-1
- initial package for Fedora