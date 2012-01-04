%global packname  aroma.light
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.22.0
Release:          1%{?dist}
Summary:          Light-weight methods for normalization and visualization of microarray data using only basic R data types

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-R.methodsS3 

BuildRequires:    R-devel tex(latex) R-R.methodsS3 

%description
Methods for microarray analysis that take basic data types such as
matrices and lists of vectors.  These methods can be used standalone, be
utilized in other packages, or be wrapped up in higher-level classes.

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
%doc %{rlibdir}/aroma.light/CITATION
%doc %{rlibdir}/aroma.light/DESCRIPTION
%doc %{rlibdir}/aroma.light/html
%doc %{rlibdir}/aroma.light/NEWS
%{rlibdir}/aroma.light/rsp
%{rlibdir}/aroma.light/data-ex
%{rlibdir}/aroma.light/Meta
%{rlibdir}/aroma.light/INDEX
%{rlibdir}/aroma.light/help
%{rlibdir}/aroma.light/R
%{rlibdir}/aroma.light/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.22.0-1
- initial package for Fedora