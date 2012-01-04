%global packname  RSEIS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.7.1
Release:          1%{?dist}
Summary:          Seismic Time Series Analysis Tools

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.7-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-RPMG 

BuildRequires:    R-devel tex(latex) R-RPMG 

%description
Multiple interactive codes to view and analyze seismic data, via spectrum
analysis, wavelet transforms, particle motion, hodograms.  Includes
general time-series tools, plotting, filtering, interactive display.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.7.1-1
- initial package for Fedora