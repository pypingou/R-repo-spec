%global packname  titan
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.16
Release:          1%{?dist}
Summary:          Titration analysis for mass spectrometry data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-16.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-boot R-tcltk R-splines R-lattice 

BuildRequires:    R-devel tex(latex) R-MASS R-boot R-tcltk R-splines R-lattice 

%description
GUI to analyze mass spectrometric data on the relative abundance of two
substances from a titration series.

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
%doc %{rlibdir}/titan/html
%doc %{rlibdir}/titan/DESCRIPTION
%{rlibdir}/titan/Meta
%{rlibdir}/titan/INDEX
%{rlibdir}/titan/data
%{rlibdir}/titan/NAMESPACE
%{rlibdir}/titan/R
%{rlibdir}/titan/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.16-1
- initial package for Fedora