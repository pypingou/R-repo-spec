%global packname  vsn
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.22.0
Release:          1%{?dist}
Summary:          Variance stabilization and calibration for microarray data

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase 
Requires:         R-methods R-affy R-limma R-lattice 

BuildRequires:    R-devel tex(latex) R-Biobase
BuildRequires:    R-methods R-affy R-limma R-lattice 


%description
The package implements a method for normalising microarray intensities,
both between colours within array, and between arrays. The method uses a
robust variant of the maximum-likelihood estimator for the stochastic
model of microarray data described in the references (see vignette). The
model incorporates data calibration (a.k.a. normalization), a model for
the dependence of the variance on the mean intensity, and a variance
stabilizing data transformation. Differences between transformed
intensities are analogous to "normalized log-ratios". However, in contrast
to the latter, their variance is independent of the mean, and they are
usually more sensitive and specific in detecting differential

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.22.0-1
- initial package for Fedora