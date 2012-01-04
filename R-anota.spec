%global packname  anota
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          ANalysis Of Translational Activity (ANOTA).

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-qvalue 
Requires:         R-multtest R-qvalue 

BuildRequires:    R-devel tex(latex) R-qvalue
BuildRequires:    R-multtest R-qvalue 


%description
Genome wide studies of translational control is emerging as a tool to
study verious biological conditions. The output from such analysis is both
the mRNA level (e.g. cytosolic mRNA level) and the levl of mRNA actively
involved in translation (the actively translating mRNA level) for each
mRNA. The standard analysis of such data strives towards identifying
differential translational between two or more sample classes - i.e.
differences in actively translated mRNA levels that are independent of
underlying differences in cytosolic mRNA levels. This package allows for
such analysis using partial variances and the random variance model. As
10s of thousands of mRNAs are analyzed in parallell the library performs a
number of tests to assure that the data set is suitable for such analysis.

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
%doc %{rlibdir}/anota/doc
%doc %{rlibdir}/anota/DESCRIPTION
%doc %{rlibdir}/anota/html
%doc %{rlibdir}/anota/NEWS
%{rlibdir}/anota/R
%{rlibdir}/anota/Meta
%{rlibdir}/anota/data
%{rlibdir}/anota/INDEX
%{rlibdir}/anota/help
%{rlibdir}/anota/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora