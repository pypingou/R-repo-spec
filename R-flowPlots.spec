%global packname  flowPlots
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          flowPlots: analysis plots and data class for gated flow cytometry data

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Graphical displays with embedded statistical tests for gated ICS flow
cytometry data, and a data class which stores "stacked" data and has
methods for computing summary measures on stacked data, such as marginal
and polyfunctional degree data.

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
%doc %{rlibdir}/flowPlots/DESCRIPTION
%doc %{rlibdir}/flowPlots/doc
%doc %{rlibdir}/flowPlots/html
%{rlibdir}/flowPlots/help
%{rlibdir}/flowPlots/Meta
%{rlibdir}/flowPlots/R
%{rlibdir}/flowPlots/extdata
%{rlibdir}/flowPlots/NAMESPACE
%{rlibdir}/flowPlots/data
%{rlibdir}/flowPlots/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora