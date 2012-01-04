%global packname  rama
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.28.0
Release:          1%{?dist}
Summary:          Robust Analysis of MicroArrays

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Robust estimation of cDNA microarray intensities with replicates. The
package uses a Bayesian hierarchical model for the robust estimation.
Outliers are modeled explicitly using a t-distribution, and the model also
addresses classical issues such as design effects, normalization,
transformation, and nonconstant variance.

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
%doc %{rlibdir}/rama/doc
%doc %{rlibdir}/rama/html
%doc %{rlibdir}/rama/DESCRIPTION
%{rlibdir}/rama/help
%{rlibdir}/rama/Meta
%{rlibdir}/rama/data
%{rlibdir}/rama/libs
%{rlibdir}/rama/R
%{rlibdir}/rama/NAMESPACE
%{rlibdir}/rama/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.28.0-1
- initial package for Fedora