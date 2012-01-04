%global packname  qtl
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.21.2
Release:          1%{?dist}
Summary:          Tools for analyzing QTL experiments

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.21-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-utils 

%description
Analysis of experimental crosses to identify genes (called quantitative
trait loci, QTLs) contributing to variation in quantitative traits.

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
%doc %{rlibdir}/qtl/CITATION
%doc %{rlibdir}/qtl/DESCRIPTION
%doc %{rlibdir}/qtl/html
%{rlibdir}/qtl/Meta
%{rlibdir}/qtl/TODO.txt
%{rlibdir}/qtl/libs
%{rlibdir}/qtl/help
%{rlibdir}/qtl/LICENSE.txt
%{rlibdir}/qtl/README.txt
%{rlibdir}/qtl/sampledata
%{rlibdir}/qtl/BUGS.txt
%{rlibdir}/qtl/R
%{rlibdir}/qtl/data
%{rlibdir}/qtl/docs
%{rlibdir}/qtl/MQM-TODO.txt
RPM build errors:
%{rlibdir}/qtl/NAMESPACE
%{rlibdir}/qtl/STATUS.txt
%{rlibdir}/qtl/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.21.2-1
- initial package for Fedora