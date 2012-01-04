%global packname  SII
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Calculate ANSI S3.5-1997 Speech Intelligibility Index

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package calculates ANSI S3.5-1997 Speech Intelligibility Index (SII),
a standard method for computing the intelligibility of speech from
acoustical measurements of speech, noise, and hearing thresholds. This
package includes data frames corresponding to Tables 1 - 4 in the ANSI
standard as well as a function utilizing these tables and user-provided
hearing threshold and noise level measurements to compute the SII score. 
The methods implemented here extend the standard computations to allow
calculation of SII when the measured frequencies do not match those
required by the standard by applying interpolation to obtain values for
the required frequencies -- Development of this package was funded by the
Center for Bioscience Education and Technology (CBET) of the Rochester
Institute of Technology (RIT).

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
%doc %{rlibdir}/SII/DESCRIPTION
%doc %{rlibdir}/SII/NEWS
%doc %{rlibdir}/SII/doc
%doc %{rlibdir}/SII/html
%{rlibdir}/SII/Meta
%{rlibdir}/SII/extdata
%{rlibdir}/SII/help
%{rlibdir}/SII/R
%{rlibdir}/SII/data
%{rlibdir}/SII/ChangeLog
%{rlibdir}/SII/NAMESPACE
%{rlibdir}/SII/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora