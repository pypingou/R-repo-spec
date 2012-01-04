%global packname  SigWinR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          SigWin-detector implementation in R

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Implementation of the SigWin-detector for the detection of regions of
increased or decreased gene expression (RIDGEs and anti-RIDGES) in
transcriptome maps and the presentation in so called RIDGEOGRAMs as
described by Marcia A. Inda et al. [BMC Res Notes 2008; 1:63]

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
%doc %{rlibdir}/SigWinR/html
%doc %{rlibdir}/SigWinR/DESCRIPTION
%{rlibdir}/SigWinR/INDEX
%{rlibdir}/SigWinR/NAMESPACE
%{rlibdir}/SigWinR/help
%{rlibdir}/SigWinR/R
%{rlibdir}/SigWinR/Meta
%{rlibdir}/SigWinR/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora