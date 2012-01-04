%global packname  RFOC
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.02
Release:          1%{?dist}
Summary:          Graphics for Spherical Distributions and Earthquake Focal Mechanisms

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-02.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-GEOmap R-RPMG R-RSEIS R-splancs 

BuildRequires:    R-devel tex(latex) R-MASS R-GEOmap R-RPMG R-RSEIS R-splancs 

%description
Graphics for statistics on a sphere, as applied to geological fault data,
crystalogaphy, earthquake focal mechanisms, radiation patterns, ternary
plots and geographical/geological maps.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.02-1
- initial package for Fedora