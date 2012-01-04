%global packname  msProcess
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Protein Mass Spectra Processing

Group:            Applications/Engineering 
License:          GNU General Public License Version 2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-graphics R-wmtsa R-robust R-XML R-stats 


BuildRequires:    R-devel tex(latex) R-methods R-graphics R-wmtsa R-robust R-XML R-stats



%description
This package provides tools for protein mass spectra processing including
data preparation, denoising, noise estimation, baseline correction,
intensity normalization, peak detection, peak alignment, peak
quantification, and various functionalities for data ingestion/conversion,
mass calibration, data quality assessment, and protein mass spectra
simulation. It also provides auxiliary tools for data representation, data
visualization, and pipeline processing history recording and retrieval.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.6-1
- initial package for Fedora