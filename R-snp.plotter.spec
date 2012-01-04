%global packname  snp.plotter
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4
Release:          1%{?dist}
Summary:          snp.plotter

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-genetics R-grid 


BuildRequires:    R-devel tex(latex) R-genetics R-grid



%description
Creates plots of p-values using single SNP and/or haplotype data. Main
features of the package include options to display a linkage
disequilibrium (LD) plot and the ability to plot multiple datasets
simultaneously. Plots can be created using global and/or individual
haplotype p-values along with single SNP p-values. Images are created as
either PDF/EPS files.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4-1
- initial package for Fedora